import re
import os
import json
import aiohttp
import asyncio
from config import *
from os import path
from bs4 import BeautifulSoup


async def fetch_groups(session) -> dict:
    """Here we get list of all groups that starts from 'ІП-'.
    """
    payload = {
        'prefixText': 'ІП-',
        'count': 10
    }
    async with session.post(GROUPS_URL, json=payload) as response:
        if not response.ok:
            response.raise_for_status()
        return await response.json()


async def fetch_group_schedule(session, group) -> str:
    payload = {
        'ctl00$MainContent$ctl00$txtboxGroup': group,
        'ctl00$MainContent$ctl00$btnShowSchedule': SCHEDULE,
        '__VIEWSTATE': VIEWSTATE,
        'hiddenInputToUpdateATBuffer_CommonToolkitScripts': COMMONTOOLKITSCRIPTS,
        'ctl00_ToolkitScriptManager_HiddenField': TOOLKITSCRIPTMANAGER,
        '__EVENTVALIDATION': EVENTVALIDATION
    }
    async with session.post(SCHEDULE_URL, data=payload) as response:
        if not response.ok:
            response.raise_for_status()
        return await response.read()


async def fetch_all_group_schedule(session, groups):
    tasks = []
    for group in groups:
        task = asyncio.create_task(fetch_group_schedule(session, group))
        tasks.append(task)
    result = await asyncio.gather(*tasks)
    return result


async def get_pairs_info(html_list: list[BeautifulSoup]) -> list:
    days = [day.text for day in html_list[0].find_all('td') if day.text]
    list_of_pairs = []
    for pair_number, item in enumerate(html_list[1:], 1):
        for index, tags in enumerate([tags for tags in item.find_all('td')][1:]):
            try:
                pairs_block = tags.find('span', attrs={'class': 'disLabel'}).find_all('a')
                learners_block = tags.find_all('a', attrs={'href': re.compile("/Schedules/ViewSchedule.*")})
                for idx in range(len(pairs_block)):
                    list_of_pairs.append({
                        "is_pair": True,
                        "day": days[index] if days else [],
                        "pair_number": pair_number,
                        "pair_name": pairs_block[idx].get('title') if pairs_block else '',
                        "pair_link": pairs_block[idx].get('href').replace(' ', '_') if pairs_block else '',
                        "learner_name": learners_block[idx].get('title') if learners_block else '',
                        "learner_link": f"http://rozklad.kpi.ua{learners_block[idx].get('href')}" if learners_block else ''
                    })
            except AttributeError:
                list_of_pairs.append({
                    "is_pair": False,
                    "day": days[index],
                    "pair_number": pair_number,
                    "pair_name": "",
                    "pair_link": "",
                    "learner_name": "",
                    "learner_link": ""
                })
    return list_of_pairs


async def get_site_content(html) -> dict:
    soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
    group_text = soup.find('span', attrs={'id': 'ctl00_MainContent_lblHeader'})
    group = re.sub(r'Розклад занять для\s*', '', group_text.text if group_text else '')
    print(group)

    try:
        first_week = soup.find('table', attrs={'id': 'ctl00_MainContent_FirstScheduleTable'}).find_all('tr')
        pairs_info_fw = await get_pairs_info(first_week)

        second_week = soup.find('table', attrs={'id': 'ctl00_MainContent_SecondScheduleTable'}).find_all('tr')
        pairs_info_sw = await get_pairs_info(second_week)
    except Exception:
        pairs_info_fw, pairs_info_sw = [], []

    return {
        "group": group,
        "first_week": pairs_info_fw,
        "second_week": pairs_info_sw
    }


async def main(path_dir: str):
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        groups = await fetch_groups(session)
        htmls = await fetch_all_group_schedule(session, groups.get('d', []))
        for idx, html in enumerate(htmls):
            content = await get_site_content(html)
            with open(f"{path_dir}/{content.get('group', idx).strip()}.json", "w") as json_file:
                json.dump(content, json_file, indent=2)


def gather_run():
    data_directory = f"{os.getcwd()}/scheduleData/"
    if not path.exists(data_directory):
        os.mkdir(data_directory)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(data_directory))
    loop.close()

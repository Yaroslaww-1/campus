import re
import json
import aiohttp
import asyncio
from config import *
from bs4 import BeautifulSoup


# async def fetch_groups(session) -> dict:
#     """Here we get list of all groups that starts from 'ІП-'.
#     """
#     payload = {
#         'prefixText': 'ІП-',
#         'count': 10
#     }
#     async with session.post(GROUPS_URL, json=payload) as response:
#         if not response.ok:
#             response.raise_for_status()
#         return await response.json()


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
                        "day": days[index],
                        "pair_number": pair_number,
                        "pair_name": pairs_block[idx].get('title'),
                        "pair_link": pairs_block[idx].get('href').replace(' ', '_'),
                        "learner_name": learners_block[idx].get('title'),
                        "learner_link": f"http://rozklad.kpi.ua{learners_block[idx].get('href')}"
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
    group = re.sub(r'Розклад занять для\s*', '', soup.find('span', attrs={'id': 'ctl00_MainContent_lblHeader'}).text)

    first_week = soup.find('table', attrs={'id': 'ctl00_MainContent_FirstScheduleTable'}).find_all('tr')
    pairs_info_fw = await get_pairs_info(first_week)

    second_week = soup.find('table', attrs={'id': 'ctl00_MainContent_SecondScheduleTable'}).find_all('tr')
    pairs_info_sw = await get_pairs_info(second_week)
    return {
        "group": group,
        "first_week": pairs_info_fw,
        "second_week": pairs_info_sw
    }


async def main():
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        # groups = await fetch_groups(session)
        # htmls = await fetch_all_group_schedule(session, groups.get('d', []))
        groups = ['ІП-96']
        htmls = await fetch_all_group_schedule(session, groups)
        for idx, html in enumerate(htmls):
            content = await get_site_content(html)
            with open(f"./schedule/{content.get('group', idx)}.json", "w", encoding='utf-8') as json_file:
                json.dump(content, json_file, indent=2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

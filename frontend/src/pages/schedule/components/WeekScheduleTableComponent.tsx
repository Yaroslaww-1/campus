import React from "react";
import { DateTime } from "luxon";

import { Event } from "@models/event.model";

import { OnePairIntervalComponent } from "./OnePairIntervalComponent";
import { ScheduleTimesColumn } from "./ScheduleTimesColumn";

import { WeekDays } from "@common/enums/schedule-week-days.enum";

import styles from "./styles.module.scss";

interface IProps {
  weekEvents: Event[];
}

export const WeekScheduleTableComponent: React.FC<IProps> = ({ weekEvents }) => {
  return (
    <div className={styles.OneTable}>
      <ScheduleTimesColumn/>
      {Object.values(WeekDays).filter(el => typeof(el) == "number").map(item =>(
        <OnePairIntervalComponent key={item} day={WeekDays[getNumberFromWeekDaysString(item)]} 
          weekDayNumber = {getNumberFromWeekDaysString(item)} 
          data={weekEvents.filter(el => checkWeekDay(el, item))}
        />
      ))
      }
    </div>
  );
};

function checkWeekDay(el:Event, item:string | WeekDays){
  return DateTime.fromISO(el.time).weekday == getNumberFromWeekDaysString(item);
}
function getNumberFromWeekDaysString(item: string | WeekDays){
  return parseInt(item.toString());
}

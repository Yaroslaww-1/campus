import React from "react";

import { Event } from "@models/event.model";

import { OnePairIntervalComponent } from "./OnePairIntervalComponent";
import { ScheduleTimesColumn } from "./ScheduleTimesColumn";

import { WeekDays } from "@common/enums/schedule-week-days.enum";

import styles from "./styles.module.scss";

interface IProps {
  weekEvents: Event[];
}

export const WeekScheduleTableComponent: React.FC<IProps> = ({ weekEvents }) => {
  const { DateTime } = require("luxon");
  return (
    <div className={styles.OneTable}>
      <ScheduleTimesColumn/>
      {Object.values(WeekDays).filter(el => typeof(el) == "number").map(item =>(
        <OnePairIntervalComponent key={item} day={WeekDays[parseInt(item.toString())]} 
          dayId = {parseInt(item.toString())} 
          data={weekEvents.filter(el => DateTime.fromISO(el.time).weekday == parseInt(item.toString()))}
        />
      ))
      }
    </div>
  );
};

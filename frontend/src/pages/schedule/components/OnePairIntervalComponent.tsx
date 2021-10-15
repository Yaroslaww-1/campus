import React from "react";
import { DateTime } from "luxon";

import { EventComponent } from "./EventComponent";
import { Event } from "@models/event.model";

import { SchedulePairsTime } from "@common/enums/schedule-pairs-times.enum";

import styles from "./styles.module.scss";

type ItemProps = {
    day: string,
    weekDayNumber: number,
    data: Event[],
};

export const OnePairIntervalComponent: React.FC<ItemProps> = ({ day, data, weekDayNumber }) => {
  return (
    <div className={styles.column}>
      <p className={styles.frsInColumn}>{day}</p>
      {Object.values(SchedulePairsTime).map( item => (
        <EventComponent key={item} event={data.filter(el =>
          checkPairTime(el, item))[0]} 
        time ={item} weekDayNumber={weekDayNumber}
        />
      ))}
    </div>
  );
};

function checkPairTime(el:Event, item:string){
  let pairTime ="";
  if (DateTime.fromISO(el.time, { zone: "utc" }).hour < 10){pairTime = "0";}
  pairTime += DateTime.fromISO(el.time, { zone: "utc" }).hour+":"+DateTime.fromISO(el.time).minute;
  return pairTime == item;
}

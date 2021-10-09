import React from "react";

import { EventComponent } from "./EventComponent";
import { Event } from "@models/event.model";

import { SchedulePairsTime } from "@common/enums/schedule-pairs-times.enum";

import styles from "./styles.module.scss";

type ItemProps = {
    day: string,
    dayId: number,
    data: Event[],
};

export const OnePairIntervalComponent: React.FC<ItemProps> = ({ day, data, dayId }) => {
  const { DateTime } = require("luxon");
  return (
    <div className={styles.column}>
      <p className={styles.frsInColumn}>{day}</p>
      {Object.values(SchedulePairsTime).map( item => (
        <EventComponent key={item} event={data.filter(el => {
          let pairTime ="";
          if (DateTime.fromISO(el.time, { zone: "utc" }).hour < 10){pairTime = "0";}
          pairTime += DateTime.fromISO(el.time, { zone: "utc" }).hour+":"+DateTime.fromISO(el.time).minute;
          return pairTime == item;})[0]} 
        time ={item} dayId={dayId}
        />
      ))}
    </div>
  );
};

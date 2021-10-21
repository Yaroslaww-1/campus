import React from "react";
import { DateTime } from "luxon";

import { EventComponent } from "./EventComponent";
import { EmptyEventComponent } from "./EmptyEventComponent";
import { Event } from "@models/event.model";

import { SchedulePairsTime } from "@common/enums/schedule-pairs-times.enum";

import styles from "./styles.module.scss";

type IProps = {
    day: string,
    weekDayNumber: number,
    events: Event[],
};

export const OnePairIntervalComponent: React.FC<IProps> = ({ day, events, weekDayNumber }) => {
  const inPairTime = (event: Event, time: string) => {
    const eventTime = DateTime.fromISO(event.time, { zone: "utc" });
    return `${eventTime.hour < 10 && "0"}${eventTime.hour}:${eventTime.minute}` == time;
  };

  const getEventsForPairTime = (events: Event[], pairTime: string) => {
    return events.filter(event => inPairTime(event, pairTime));
  };

  return (
    <div className={styles.column}>
      <p className={styles.frsInColumn}>{day}</p>
      {Object.values(SchedulePairsTime).map(pairTime => (
        getEventsForPairTime(events, pairTime).length > 0
          ? <EventComponent
            key={pairTime}
            event={getEventsForPairTime(events, pairTime)[0]} 
            time ={pairTime}
            weekDayNumber={weekDayNumber}
          />
          : <EmptyEventComponent />
      ))}
    </div>
  );
};



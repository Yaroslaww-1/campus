import React from "react";
import { Event } from "@models/event.model";

import styles from "./styles.module.scss";

interface IEvent {
  key: number;
  dayId: number;
  event: Event[];
  time: string;
}

export const EventComponent: React.FC<IEvent> = ({ dayId, event, time }) => {
  const one_events = (event.filter(el => el.time.substr(12, 5) == time ))
    .filter(el => new Date(el.time.substr(0, 10)).getDay() == dayId);

  let one_event:Event;
  if (one_events.length > 0){
    one_event = one_events[0];
  }
  else{
    one_event = { id: "",
      name: "",
      description: "Empty",
      time: "",
      type: "" };
  }
  return (
    <div className={styles.tmpP}>
      <h3 className={styles.sbjName}>{one_event.name}</h3>
      <div className={styles.teacherName}>
        <p className={styles.teacherFullName}>Teacher name</p>
      </div>
      <p className={styles.typeOfPair}>{one_event.type}</p>
      <div className={styles.description}>Опис
        <p className={styles.pairDesk}>{one_event.description}</p>
      </div>
    </div>
  );
};
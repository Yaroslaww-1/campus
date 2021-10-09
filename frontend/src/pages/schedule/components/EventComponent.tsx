import React from "react";

import { Event } from "@models/event.model";

import styles from "./styles.module.scss";

interface IEvent {
  key: string;
  dayId: number;
  event: Event;
  time: string;
}

export const EventComponent: React.FC<IEvent> = ({ dayId, event, time }) => {
  let oneEvent:Event;
  if (event){
    oneEvent = event;
    console.log("");
  }
  else{
    oneEvent = { id: "",
      name: "",
      description: "",
      time: "",
      type: "" };
  }
  //console.log(event);
  return (
    <div className={styles.eventComponentCell}>
      <h3 className={styles.sbjName}>{oneEvent.name || "..."}</h3>
      <div className={styles.teacherName}>...
        <p className={styles.teacherFullName}>Teacher name</p>
      </div>
      <p className={styles.typeOfPair}>{oneEvent.type || "..."}</p>
      <div className={styles.description}>Description
        <p className={styles.pairDesk}>{oneEvent.description || "..."}</p>
      </div>
    </div>
  );
};

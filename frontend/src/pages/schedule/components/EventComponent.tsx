import React from "react";

import { Event } from "@models/event.model";

import styles from "./styles.module.scss";

interface IProps {
  key: string;
  weekDayNumber: number;
  event: Event;
  time: string;
}

export const EventComponent: React.FC<IProps> = ({ weekDayNumber, event, time }) => {
  return (
    <div className={styles.eventComponentCell}>
      <h3 className={styles.sbjName}>{event.name || "..."}</h3>
      <div className={styles.teacherName}>...
        <p className={styles.teacherFullName}>Teacher name</p>
      </div>
      <p className={styles.typeOfPair}>{event.type || "..."}</p>
      <div className={styles.description}>Description
        <p className={styles.pairDesk}>{event.description || "..."}</p>
      </div>
    </div>
  );
};

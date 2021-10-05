import React from "react";

import { Event } from "@models/event.model";

import {  WeekScheduleTableComponent } from "./WeekScheduleTableComponent";

import styles from "./styles.module.scss";

interface IProps {
  events: Event[];
}
//filter for week is temporary solution, we need done db or proper events structure
export const ScheduleTables: React.FC<IProps> = ({ events }) => { 
  return (
    <div className={styles.allTables}>
      <h1>Перший тиждень</h1>
      <WeekScheduleTableComponent weekEvents={events}/>
      <h1>Другий тиждень</h1>
      <WeekScheduleTableComponent weekEvents={events}/>
    </div>
  );
};

import React from "react";
import { useEffect } from "react";

import { Event } from "@models/event.model";
import { timesState } from "../schedule.state";

import { OneRowOfTable } from "./OneRowOfTable";
import { HeaderRow } from "./HeaderRow";

import styles from "./styles.module.scss";

interface IProps {
  weekEvents: Event[];
}

export const WeekScheduleTableComponent: React.FC<IProps> = ({ weekEvents }) => {
  useEffect(()=> {
    timesState.fetchTimes();
  }, []);
  return (
    <div className={styles.OneTable}>
      <HeaderRow/>
      {timesState.pairsTime.map(item =>(
        <OneRowOfTable key={item.id} time={item.time} data={weekEvents}/>
      ))}
    </div>
  );
};
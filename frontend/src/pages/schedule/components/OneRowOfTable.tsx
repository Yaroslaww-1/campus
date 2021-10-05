import React from "react";

import { EventComponent } from "./EventComponent";
import { Event } from "@models/event.model";
import { useEffect } from "react";

import { datesState } from "../schedule.state";

import styles from "./styles.module.scss";

type ItemProps = {
    key: number,
    time: string,
    data: Event[],
};

export const OneRowOfTable: React.FC<ItemProps> = ({ time, data }) => {
  useEffect(()=> {
    datesState.fetchDays();
  }, []);
  return (
    <div className={styles.row}>
      <p className={styles.frsInRow}>{time}</p>
      {datesState.days.map( item => (
        <EventComponent key={item.id} event={data} time ={time} dayId={item.id}/>
      ))}
    </div>
  );
};
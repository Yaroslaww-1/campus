import React from "react";
import { useEffect } from "react";

import { datesState } from "../schedule.state";

import styles from "./styles.module.scss";

export const HeaderRow: React.FC = () => {
  useEffect(()=> {
    datesState.fetchDays();
  }, []);
  return (
    <div className={styles.row} >
      <p className={styles.frsInRow}></p>
      {datesState.days.map(item => (
        <p key={item.id} className={styles.dayP}>{item.name}</p>
      ))}
    </div>
  );
};
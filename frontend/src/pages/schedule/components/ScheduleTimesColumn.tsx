import React from "react";

import { SchedulePairsTime } from "@common/enums/schedule-pairs-times.enum";
import { getValuesFromEnum } from "@common/helpers/enum.helper";

import styles from "./styles.module.scss";

export const ScheduleTimesColumn: React.FC = () => {
  return (
    <div className={`${styles.column} ${styles.firstColumn}`} >
      <p className={styles.frsInColumn}></p>
      {getValuesFromEnum(SchedulePairsTime).map(item => (
        <p key={item} className={styles.timeP}>{item}</p>
      ))}
    </div>
  );
};

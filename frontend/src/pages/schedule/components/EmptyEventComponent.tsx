import React from "react";

import styles from "./styles.module.scss";

export const EmptyEventComponent: React.FC = () => {
  return (
    <div className={styles.eventComponentCell}>
      <h3 className={styles.sbjName}>...</h3>
      <div className={styles.teacherName}>...
        <p className={styles.teacherFullName}>Teacher name</p>
      </div>
      <p className={styles.typeOfPair}>...</p>
      <div className={styles.description}>Description
        <p className={styles.pairDesk}>...</p>
      </div>
    </div>
  );
};

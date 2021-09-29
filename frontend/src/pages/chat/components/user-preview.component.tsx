import React from "react";
import styles from "./styles.module.scss";

import { User } from "@models/user.model";

export const UserPreview: React.FC<User> = props => {
  return (
    <div className={styles.userItem}>
      <div className={styles.nameRoleWrapper}>
        <div className={styles.name}>{props.name}</div>
        <div className={styles.role}>{props.role}</div>
      </div>
      <div className={styles.statu}>{props.status}</div>
    </div>
  );
};

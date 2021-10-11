import React from "react";
import styles from "./styles.module.scss";

import { User } from "@models/user.model";

export const UserPreview: React.FC<User> = props => {
  return (
    <div
      className={styles.userItem}
      onClick={() => {
        window.location.href = `/users/${props.id}` || "/users";
      }}
    >
      <div className={styles.nameRoleWrapper}>
        <div className={styles.name}>{props.name}</div>
        <div className={styles.role}>{props.role}</div>
      </div>
      <div className={styles.status}>{props.status}</div>
    </div>
  );
};

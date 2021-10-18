import React from "react";

import { User } from "@models/user.model";

import styles from "./styles.module.scss";
import userImg from "../../../assets/user.png";

export const UserProfile: React.FC<User> = props => {
  return (
    <div className={styles.mainBlock}>
      <img className={styles.userImg} src={userImg} alt={props.id}></img>
      <div className={styles.infoBlock}>
        <div className={styles.name}>{props.name}</div>
        <div className={styles.info}>Role: {props.role}</div>
        <div
          className={styles.email}
          onClick={() => {
            navigator.clipboard.writeText(props.email || "");
          }}
        >
          Email: {props.email}
        </div>
        <div className={styles.info}>Status: </div>
      </div>
    </div>
  );
};

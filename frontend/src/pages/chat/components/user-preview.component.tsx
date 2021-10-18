import React from "react";
import { useHistory } from "react-router-dom";

import styles from "./styles.module.scss";

import { User } from "@models/user.model";

import userImg from "../../../assets/user.png";

export const UserPreview: React.FC<User> = props => {
  const history = useHistory();

  const routeChange = () => {
    const path: string = `/user/${props.id}`;
    history.push(path);
  };

  return (
    <div className={styles.userItem} onClick={routeChange}>
      <div className={styles.imgUser}>
        <img className={styles.imgUser} src={userImg} alt=""></img>
      </div>
      <div className={styles.mainInfoWrapper}>
        <div className={styles.nameRoleWrapper}>
          <div className={styles.name}>{props.name}</div>
          <div className={styles.role}>{props.role}</div>
        </div>
        <div className={styles.status}>{props.status}</div>
      </div>
    </div>
  );
};

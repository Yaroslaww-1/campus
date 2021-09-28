import React from "react";
import styles from "./styles.module.scss";

interface UserProps {
  name: string;
  role: string;
  status: string;
}

export const UserPreview: React.FC<UserProps> = props => {
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

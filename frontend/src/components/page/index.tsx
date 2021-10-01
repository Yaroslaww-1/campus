import React from "react";

import styles from "./styles.module.scss";

interface IProps {
  classes?: {
    root?: string;
  }
}

export const PageComponent: React.FC<IProps> = ({
  children,
  classes = {},
}) => {
  return (
    <div className={`${styles.page} ${classes.root || ""}`}>
      {children}
    </div>
  );
};

import React from "react";

import styles from "../styles.module.scss";

interface IProps {
  name: string;
  imgSrc: string;
  redirectToUrl: string;
}

export const Section: React.FC<IProps> = props => {
  return (
    <div className={styles.sectionWrapper}>
      <a href={props.redirectToUrl} title={props.name}>
        <img
          className={styles.imgLogo}
          src={props.imgSrc}
          alt={props.name}
        ></img>
      </a>
    </div>
  );
};

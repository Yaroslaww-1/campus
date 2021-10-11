import React from "react";
import { Section } from "./components/section.component";

import styles from "./styles.module.scss";

import homeLogo from "../../assets/home.png";
import chatLogo from "../../assets/chat.png";
import coursesLogo from "../../assets/courses.png";

export const Header: React.FC = () => {
  return (
    <div className={styles.header}>
      <div className={styles.mainBut}>
        <Section name={"Home"} href={"/posts"} imgSrc={homeLogo}></Section>
        <Section name={"Chats"} href={"/users"} imgSrc={chatLogo}></Section>
        <Section name={"Courses"} href={"/courses"} imgSrc={coursesLogo}></Section>
      </div>
    </div>
  );
};

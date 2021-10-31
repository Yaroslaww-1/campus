import api from "@api/api.helper";
import React, { useState } from "react";

import styles from "./styles.module.scss";

const endpoint = "/chat";

export const CreateChat: React.FC = () => {
  const [chatName, setChatName] = useState("");
  const [chatAvatar, setChatAvatar] = useState("");
  const [chatUsers, setUsers] = useState("");

  function onSubmit() {
    const formData = new FormData();
    formData.append("name", chatName);
    formData.append("name", chatAvatar);
    formData.append("name", chatUsers);
    api.put(endpoint, formData);
  }
  function lookForUsers(params : string){};
  // TODO: add img to char avatar, save it when it change
  // TODO2: create structure of user in search result, if it`s will be list of users then move it to another component (for loop like in schedule)
  return(
    <div className={styles.container}>
      <h1 className={styles.chatCreateTitle}>Create new chat</h1>
      <form className={styles.chatCreateForm} onSubmit={onSubmit}>
        <div className={styles.image}>
          <input type="button" className={styles.photoBtn}></input>
        </div>
        <input type="text" className={styles.inputName} placeholder={"Chat name"}
          required onChange={data => setChatName(data.target.value)}
        />
        <div className={styles.usersList}>
          <div className={styles.usersSearchArea}>
            <input type="text" className={styles.userSearch} placeholder={"User name"}
              required onChange={data => lookForUsers("")}
            />
            <input type="button" className={styles.searchBtn}></input>
          </div>
          <div className={styles.fullListOfUsers}>
            <div className={styles.TODO2}/>
          </div>
        </div>
        <input className={styles.submitBtn} type="submit" name="Create" value="Create"/>
      </form>
    </div>);
};
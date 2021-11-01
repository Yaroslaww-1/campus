import React, { useState } from "react";

import { PostsService } from "@api/services/posts.service";

import styles from "./styles.module.scss";

export const CreatePost: React.FC = () => {
  const [name, setName] = useState("");
  const [content, setContent] = useState("");

  function onSubmit() {
    PostsService.createPost(name, content);
  }

  return (
    <div className={styles.container}>
      <div>
        <h1 className={styles.cardTitle}>Create Post: </h1>
        <form className={styles.cardForm} onSubmit={onSubmit}>
          <div className="input">
            <input
              type="text"
              className={styles.inputField}
              placeholder={"Name"}
              required
              onChange={e => setName(e.target.value)}
            />
          </div>
          <div className="input">
            <textarea
              className={styles.inputTextArea}
              placeholder={"Content"}
              required
              onChange={e => setContent(e.target.value)}
            />
          </div>
          <input
            className={styles.btn}
            type="submit"
            name="Create"
            value="Create"
          />
        </form>
      </div>
    </div>
  );
};

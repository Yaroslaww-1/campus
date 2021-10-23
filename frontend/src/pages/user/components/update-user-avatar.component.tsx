import React, { useState } from "react";

import api from "../../../api/api.helper";

import { User } from "@models/user.model";

export const UpdateUserAvatar: React.FC<User> = props => {
  const BASE_URL = process.env.REACT_APP_API_URL;
  const endpoint = "users";

  const [id, setId] = useState("");
  const [avatar, setAvatar] = useState<File>();

  function onSubmit() {
    const formData = new FormData();
    formData.append("id", id);
    formData.append("avatar", avatar || "");
    api.put(BASE_URL + endpoint, formData);
  }

  return (
    <div>
      <form id="formEl" onSubmit={onSubmit}>
        <label>Id: </label>
        <input
          type="text"
          name="id"
          value={id}
          onChange={e => setId(e.target.value)}
        />
        <br />
        <label>Filename: </label>
        <input
          type="file"
          name="avatar"
          onChange={e => setAvatar(e.target.files![0])}
        />
        <br />
        <input type="submit" name="submit" value="Submit" />
      </form>
    </div>
  );
};

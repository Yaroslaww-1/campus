import React from "react";

import api from "../../../api/api.helper";

import { User } from "@models/user.model";

export const UpdateUserAvatar: React.FC<User> = props => {
  const BASE_URL = process.env.REACT_APP_API_URL;
  const endpoint = "users";

  return (
    <div>
      <form
        id="formEl"
        onSubmit={() => {
          api.put(
            BASE_URL + endpoint,
            new FormData(document.querySelector("form") || undefined),
          );
        }}
      >
        <label>Id: </label>
        <input type="text" name="id" />
        <br />
        <label>Filename: </label>
        <input type="file" name="avatar" />
        <br />
        <input type="submit" name="submit" value="Submit" />
      </form>
    </div>
  );
};

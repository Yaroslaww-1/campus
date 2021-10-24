import React, { useState } from "react";

import api from "../../../api/api.helper";
import { FileUploadField } from "./file-upload-field";

export const UpdateUserAvatar: React.FC = () => {
  const BASE_URL = process.env.REACT_APP_API_URL;
  const endpoint = "users";

  const [id, setId] = useState("");
  let file: File;

  function onSubmit() {
    const formData = new FormData();
    formData.append("id", id);
    formData.append("avatar", file || "");
    api.put(BASE_URL + endpoint, formData);
  }

  function handleFileUpload(newFile: File) {
    file = newFile;
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
        <FileUploadField onUpload={handleFileUpload} name={"avatar"} />
        <br />
        <input type="submit" name="submit" value="Submit" />
      </form>
    </div>
  );
};

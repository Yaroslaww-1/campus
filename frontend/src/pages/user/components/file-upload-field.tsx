import React from "react";

interface IFileUpload {
  name: string;
  onUpload: (file: File) => void;
}

export const FileUploadField: React.FC<IFileUpload> = props => {
  return (
    <input
      type="file"
      name={props.name}
      onChange={e => {
        props.onUpload(e.target.files![0]);
      }}
    />
  );
};

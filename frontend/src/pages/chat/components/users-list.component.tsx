import React from "react";
import { UserPreview } from "./user-preview.component";

interface UserListProps {
  userList: {
    id: string;
    name: string;
    role: string;
    status: string;
  }[];
}

export const UserList: React.FC<UserListProps> = props => {
  return (
    <React.Fragment>
      {props.userList.map(item => {
        return (
          <UserPreview
            key={item.id}
            name={item.name}
            role={item.role}
            status={item.status}
          />
        );
      })}
    </React.Fragment>
  );
};

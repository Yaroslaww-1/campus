import { PageComponent } from "@components/index";
import { UserList } from "./components/users-list.component";

export const UsersPage: React.FC = () => {
  const userList = [
    { id: "1", name: "Nazarii Striletskyi", role: "student", status: "online" },
    { id: "2", name: "Yaroslav Borodaienko", role: "student", status: "online" },
    { id: "3", name: "Clown", role: "lecturer", status: "offline" },
    { id: "4", name: "Circus", role: "admin", status: "offline" },
  ];
  return (
    <PageComponent>
      <UserList userList={userList} />
    </PageComponent>
  );
};

import { useEffect } from "react";
import { observer } from "mobx-react-lite";

import { usersState, UsersState } from "@pages/chat/users.state";

import { UserPreview } from "@pages/chat/components/user-preview.component";

import styles from "../../components/styles.module.scss";

interface IProps {
  state: UsersState;
}

const UsersListContainerContent: React.FC<IProps> = observer(({ state }) => {
  useEffect(() => {
    state.fetchUsers();
  }, []);

  return (
    <div className={styles.userListWrapper}>
      <div className={styles.userList}>
        {state.users.map((user, index) => {
          return (
            <UserPreview
              key={index}
              id={user.id}
              name={user.name}
              role={user.role}
              status={user.status}
            />
          );
        })}
      </div>
    </div>
  );
});

export const UsersListContainer: React.FC = () => (
  <UsersListContainerContent state={usersState} />
);

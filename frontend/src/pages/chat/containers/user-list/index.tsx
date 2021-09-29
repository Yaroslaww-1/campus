import { useEffect } from "react";
import { observer } from "mobx-react-lite";

import { usersState, UsersState } from "@pages/chat/users.state";

import { PageComponent } from "@components/index";
import { UserPreview } from "@pages/chat/components/user-preview.component";

interface IProps {
  state: UsersState;
}

const UsersListContainerContent: React.FC<IProps> = observer(({ state }) => {
  useEffect(() => {
    state.fetchUsers();
  }, []);

  return (
    <PageComponent>
      {state.users.map(user => {
        return (
          <UserPreview
            key={user.id}
            name={user.name}
            role={user.role}
            status={user.status}
          />
        );
      })}
    </PageComponent>
  );
});

export const UsersListContainer: React.FC = () => (
  <UsersListContainerContent state={usersState} />
);

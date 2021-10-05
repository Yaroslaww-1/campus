import { PageComponent } from "@components/index";
import { UsersListContainer } from "./containers/user-list";

export const UsersPage: React.FC = () => {
  return (
    <PageComponent>
      <UsersListContainer />
    </PageComponent>
  );
};

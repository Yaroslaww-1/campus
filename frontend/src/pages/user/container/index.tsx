import { useEffect } from "react";
import { observer } from "mobx-react-lite";

import { userProfileState, UserProfileState } from "../user-profile.state";

import { UserProfile } from "../components/profile.component";

interface IProps {
  state: UserProfileState;
}

const UserProfileContainerContent: React.FC<IProps> = observer(({ state }) => {
  useEffect(() => {
    state.fetchUserProfile(`${window.location.pathname.replace("/user/", "")}`);
  }, []);

  return (
    <UserProfile
      id={state.userProfile.id}
      name={state.userProfile.name}
      role={state.userProfile.role}
      status={state.userProfile.status}
      email={state.userProfile.email}
    ></UserProfile>
  );
});

export const UserProfileContainer: React.FC = () => (
  <UserProfileContainerContent state={userProfileState} />
);

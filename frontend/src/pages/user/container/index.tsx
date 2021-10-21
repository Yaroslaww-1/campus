import { useEffect } from "react";
import { useParams } from "react-router-dom";
import { observer } from "mobx-react-lite";

import { userProfileState, UserProfileState } from "../user-profile.state";

import { UserProfile } from "../components/profile.component";

interface IProps {
  state: UserProfileState;
}

interface IUrlParams {
  id: string;
}

const UserProfileContainerContent: React.FC<IProps> = observer(({ state }) => {
  const { id } = useParams<IUrlParams>();

  useEffect(() => {
    state.fetchUserProfile(id);
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

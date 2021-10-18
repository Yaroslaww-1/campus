import { runInAction, makeAutoObservable } from "mobx";
import { UserProfileService } from "@api/services/user-profile.service";

import { FetchStatus } from "@common/enums/fetch-status.enum";

import { User } from "@models/user.model";

export class UserProfileState {
  userProfile: User = {
    name: "",
    role: "",
    status: "",
  };
  state = FetchStatus.PENDING;

  constructor() {
    makeAutoObservable(this);
  }

  async fetchUserProfile(id: string) {
    this.state = FetchStatus.PENDING;
    try {
      const userProfile = await UserProfileService.getUser(id);
      runInAction(() => {
        this.userProfile = userProfile;
        this.state = FetchStatus.DONE;
      });
    } catch (e) {
      runInAction(() => {
        this.state = FetchStatus.ERROR;
      });
    }
  }
}

export const userProfileState = new UserProfileState();

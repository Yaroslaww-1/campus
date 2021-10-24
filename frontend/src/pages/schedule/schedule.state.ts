import { runInAction, makeAutoObservable } from "mobx";
import { EventService } from "@api/services/event.service";

import { FetchStatus } from "@common/enums/fetch-status.enum";
import { Event } from "@models/event.model";

export class EventsState {
  events: Event[] = [];
  state = FetchStatus.PENDING;

  constructor() {
    makeAutoObservable(this);
  }

  async fetchEvents() {
    this.events = [];
    this.state = FetchStatus.PENDING;
    try {
      const events = await EventService.getEvents();
      runInAction(() => {
        this.events = events;
        this.state = FetchStatus.DONE;
      });
    } catch (e) {
      runInAction(() => {
        this.state = FetchStatus.ERROR;
      });
    }
  }
}

export const eventsState = new EventsState();

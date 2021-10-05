import { runInAction, makeAutoObservable } from "mobx";
import { EventService, DaysInWeek, PairsTime } from "@api/services/event.service";

import { FetchStatus } from "@common/enums/fetch-status.enum";
import { Event, DayInWeek, PairTime } from "@models/event.model";

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

export class DaysState {
  days: DayInWeek[] = [];
  state = FetchStatus.PENDING;

  async fetchDays() {
    this.days = [];
    this.state = FetchStatus.PENDING;
    try {
      const days = await DaysInWeek.getDays();
      runInAction(() => {
        this.days = days;
        this.state = FetchStatus.DONE;
      });
    } catch (e) {
      runInAction(() => {
        this.state = FetchStatus.ERROR;
      });
    }
  }
}

export const datesState = new DaysState();

export class TimesState {
  pairsTime: PairTime[] = [];
  state = FetchStatus.PENDING;

  async fetchTimes() {
    this.pairsTime = [];
    this.state = FetchStatus.PENDING;
    try {
      const pairsTime = await PairsTime.getPairsTime();
      runInAction(() => {
        this.pairsTime = pairsTime;
        this.state = FetchStatus.DONE;
      });
    } catch (e) {
      runInAction(() => {
        this.state = FetchStatus.ERROR;
      });
    }
  }
}

export const timesState = new TimesState();
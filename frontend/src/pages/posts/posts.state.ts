import { runInAction, makeAutoObservable } from "mobx";
import { PostsService } from "../../api/services/posts.service";

import { FetchStatus } from "../../common/enums/fetch-status.enum";
import { Post } from "../../models/post.model";

export class PostsState {
  posts: Post[] = [];
  state = FetchStatus.PENDING;

  constructor() {
    makeAutoObservable(this);
  }

  async fetchPosts() {
    this.posts = [];
    this.state = FetchStatus.PENDING;
    try {
      const posts = await PostsService.getPosts();
      runInAction(() => {
        this.posts = posts;
        this.state = FetchStatus.DONE;
      });
    } catch (e) {
      runInAction(() => {
        this.state = FetchStatus.ERROR;
      });
    }
  }
}

export const postsState = new PostsState();

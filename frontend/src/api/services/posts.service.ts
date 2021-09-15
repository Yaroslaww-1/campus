import { v4 } from "uuid";

import { Post } from "../../models/post.model";
import api from "../api.helper";

const endpoint = "posts";

export class PostsService {
  static async getPosts(): Promise<Post[]> {
    // TODO: uncomment
    // const posts = await api.get<Post[]>(endpoint);
    const posts = [
      {
        id: v4(),
        name: "Dopka incoming",
      },
      {
        id: v4(),
        name: "Dopka cancelled!",
      },
    ];
    return posts;
  }
}
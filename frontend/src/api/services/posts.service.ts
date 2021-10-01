import { Post } from "../../models/post.model";
import api from "../api.helper";

const endpoint = "posts";

export class PostsService {
  static async getPosts(): Promise<Post[]> {
    const posts = await api.get<Post[]>(endpoint);
    return posts;
  }
}
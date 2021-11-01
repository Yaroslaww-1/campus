import { Post } from "../../models/post.model";
import api from "../api.helper";

const endpoint = "learn/posts";

export class PostsService {
  static async getPosts(): Promise<Post[]> {
    const posts = await api.get<Post[]>(endpoint);
    return posts;
  }
  static async createPost(name: string, content: string): Promise<void> {
    const formData = new FormData();
    formData.append("name", name);
    formData.append("content", content);
    api.post(endpoint, formData);
  }
}

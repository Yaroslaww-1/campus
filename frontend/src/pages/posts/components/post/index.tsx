import { getRandomInt, getRandomDate } from "@common/helpers/random.helper";
import { Post } from "@models/post.model";

import { PostImageComponent } from "../post-image";

import styles from "./styles.module.scss";

interface IProps {
  post: Post;
}

export const PostComponent: React.FC<IProps> = ({ post }) => {
  const randomImageUrl = `https://picsum.photos/id/${getRandomInt(1, 200)}/2000/2000`;
  const randomDate = getRandomDate();

  return (
    <div className={styles.root}>
      <p className={styles.name}>{post.name}</p>
      <p className={styles.content}>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Unde, excepturi atque. Nulla et molestiae officiis in totam? Debitis, velit, excepturi asperiores voluptas exercitationem maiores nisi eveniet voluptatum magnam odit mollitia.</p>
      <PostImageComponent src={randomImageUrl} />
      <div className={styles.footer}>
        <p className={styles.createdAt}>{randomDate.toUTCString()}</p>
      </div>
    </div>
  );
};

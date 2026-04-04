// 1516번: 게임 개발

import java.io.*;
import java.util.*;

class Main {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());

            Node node = Node.get(i);
            node.cost = Integer.parseInt(st.nextToken());
            node.minDist = node.cost;

            while (true) {
                int p = Integer.parseInt(st.nextToken());
                if (p == -1)
                    break;
                Node.get(p).addChild(node);
            }
        }

        Queue<Node> q = new ArrayDeque<>();

        for (int i = 1; i <= N; i++) {
            Node node = Node.get(i);
            if (node.inDegree == 0)
                q.offer(node);
        }

        while (!q.isEmpty()) {
            Node node = q.poll();
            for (Node child : node.children) {
                child.minDist = Math.max(
                    child.minDist,
                    node.minDist + child.cost
                );
                child.inDegree--;
                if (child.inDegree == 0)
                    q.offer(child);
            }
        }

        for (int nodeId = 1; nodeId <= N; nodeId++)
            System.out.println(Node.get(nodeId).minDist);
    }
}

class Node {
    static final int MAX_N = 500;
    static final Node[] instances = new Node[MAX_N+1];

    static {
        for (int nodeId = 1; nodeId <= MAX_N; nodeId++)
            instances[nodeId] = new Node();
    }

    static Node get(int id) {
        return instances[id];
    }

    int cost = 0;
    int minDist = 0;
    List<Node> children = new ArrayList<>();
    int inDegree = 0;

    void addChild(Node childNode) {
        children.add(childNode);
        childNode.inDegree++;
    }
}

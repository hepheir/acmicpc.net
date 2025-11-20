// 24791번: Victory Through Synergy

import java.io.*;
import java.util.*;

class Main {
    private static class Player {
        public String name = null;
        public String nation = null;
        public String league = null;
        public String team = null;
        private Node node = null;

        public boolean hasNode() {
            return this.node != null;
        }

        public int getSynergy(Player player) {
            if (nation.equals(player.nation) && team.equals(player.team)) {
                return 3;
            }
            if (nation.equals(player.nation) && league.equals(player.league)) {
                return 2;
            }
            if (team.equals(player.team)) {
                return 2;
            }
            if (league.equals(player.league)) {
                return 1;
            }
            if (nation.equals(player.nation)) {
                return 1;
            }
            return 0;
        }
    }

    private static class Node {
        private Player player = null;
        public List<Node> links = new ArrayList<>();

        public void setPlayer(Player player) {
            this.player = player;
            this.player.node = this;
        }

        public void clearPlayer() {
            this.player.node = null;
            this.player = null;
        }

        public int getDegree() {
            return links.size();
        }

        public int getSynergy() {
            int synergy = 0;
            for (Node node : links) {
                synergy += player.getSynergy(node.player);
            }
            return synergy;
        }
    }

    private static final int MAX_NODES = 10;
    private static final BufferedReader br;
    private static final Node[] nodes;
    private static final Player[] players;

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
        nodes = new Node[MAX_NODES];
        players = new Player[MAX_NODES];
        for (int i = 0; i < MAX_NODES; i++) {
            nodes[i] = new Node();
            players[i] = new Player();
        }
    }

    public static void main(String[] args) throws IOException {
        int c = Integer.parseInt(br.readLine());

        while (c-- > 0) {
            String[] tokens = br.readLine().split(" ");
            int a = Integer.parseInt(tokens[0]);
            int b = Integer.parseInt(tokens[1]);
            nodes[a].links.add(nodes[b]);
            nodes[b].links.add(nodes[a]);
        }

        for (int i = 0; i < MAX_NODES; i++) {
            String[] tokens = br.readLine().split(" ");
            players[i].name = tokens[0];
            players[i].nation = tokens[1];
            players[i].league = tokens[2];
            players[i].team = tokens[3];
        }

        if (canMakePerfectTeam()) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }
    }

    private static boolean canMakePerfectTeam() {
        return tryMakePerfectTeamBT(0);
    }

    private static boolean tryMakePerfectTeamBT(int nodeId) {
        // Backtracking
        if (nodeId == MAX_NODES) {
            return isPerfectTeam();
        }
        Node node = nodes[nodeId];
        for (Player player : players) {
            if (player.hasNode()) {
                continue;
            }
            node.setPlayer(player);
            if (tryMakePerfectTeamBT(nodeId + 1)) {
                return true;
            }
            node.clearPlayer();
        }
        return false;
    }

    private static boolean isPerfectTeam() {
        for (Node node : nodes) {
            if (node.getSynergy() < node.getDegree()) {
                return false;
            }
        }
        return true;
    }
}

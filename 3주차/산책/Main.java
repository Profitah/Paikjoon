import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static List<List<Integer>> graph;
    static int[] inOut;
    static boolean[] visited;
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        inOut = new int[n+1];
        int route_count = 0;

        graph = new ArrayList<>();
        for(int i=0;i<=n;i++){
            graph.add(new ArrayList<>());
        }

        String A = br.readLine();
        for(int i=1;i<n+1;i++){
            inOut[i] = Integer.parseInt(String.valueOf(A.charAt(i-1)));
        }

        for(int i=0;i<n-1;i++){
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            graph.get(from).add(to);
            graph.get(to).add(from);

            if(inOut[from]==1 && inOut[to]==1){ //실내끼리 인접하면 경로를 2개 더함
                route_count += 2;
            }
        }

        visited = new boolean[n+1];
        for(int i=1;i<=n;i++){
            int in = 0; //실내의 수
            if(inOut[i]==0) { 
                if(!visited[i]){
                    visited[i] = true;
                    in = dfs(i); //실외를 만나면 탐색
                }
            }
            route_count += in*(in-1); //실내(실내-1)
        }

        System.out.println(route_count);
    }
    private static int dfs(int start) {
        int in = 0;

        for(int v : graph.get(start)){
            if(inOut[v]==0){ 
                if(!visited[v]) {
                    visited[v] = true;
                    in += dfs(v); //실외면 계속 탐색
                }
            }
            else{ //실내라면
                in++;
            }
        }
        return in;
    }
}
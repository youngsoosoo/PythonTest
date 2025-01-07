class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        for (int i = 0; i < skill_trees.length; i++) {
            
			String s = skill_trees[i].replaceAll("[^" + skill + "]", "");
            
			for (int j = 0; j < skill.length() + 1; j++) {
				String subSkill = skill.substring(0, j);
				if (s.equals(subSkill)) {
					answer++;
					break;
				}
			}
        }
        
        return answer;
    }
}
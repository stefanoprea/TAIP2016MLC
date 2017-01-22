package sim;

import org.apache.commons.lang3.StringUtils;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONTokener;

public class Main {
	public static void main(String args[]) throws IOException, JSONException{
		String word1=args[0].toLowerCase();
		String word2=args[1].toLowerCase();

		if(word1.equals(word2)){
			System.out.println("4");//if the words are identical
		}
		else{
			//word1 should be shorter, word2 longer
			//the inversion is done in order to save time on some future comparisons
			if(word1.length()>word2.length()){
				String aux=word1;
				word1=word2;
				word2=aux;
			}

			if(areAntonyms(word1, word2))
				System.out.println("0");
			else{
				int score=0;
				try{
					score=calculateScore(word1, word2);
				}
				finally{
					System.out.println(score);
				}	
			}
		}
	}


	/*
	 * Each word may have one or more definitions. 
	 * We compare all the possible pairs of definitions and save the biggest score.
	 */
	private static int calculateScore(String word1, String word2) throws IOException, JSONException {

		double score=0;  
		double maxScore=0;
		double sameRoot=0;

		if(word2.contains(word1))
			sameRoot=0.2; //this value will be added later

		String json1=getApiResult(word1);
		String json2=getApiResult(word2);
		ArrayList<String> definitions1=getDefinitions(json1);
		ArrayList<String> definitions2=getDefinitions(json2);
		if(definitions1!=null || definitions2!=null|| definitions1.size()!=0 || definitions2.size()!=0){ //if we have no definitions

			for(int i=0; i<definitions1.size(); i++)
				for(int j=0; j<definitions2.size(); j++){
					String def1=definitions1.get(i);
					String def2=definitions2.get(j);

					//find the longer definition and calculate the Levenshtein distance
					String longer=def1;
					String shorter=def2;
					if (def1.length() < def2.length()) { 
						longer = def2; 
						shorter = def1;
					}

					int longerLength = longer.length();
					if (longerLength == 0) { 
						score=4; /* both strings are zero length */ 
					}
					else score= (longerLength - StringUtils.getLevenshteinDistance(longer, shorter)) / (double) longerLength;
					//increase the score if a word is found in the definition of the other
					score+=sameRoot;
					if(def1.contains(word2)||(def2.contains(word1)))
						score+=0.2;
					if(score>maxScore)
						maxScore=score;
					//System.out.println(""+score);
				}
		}
		//System.out.println("Max score:"+maxScore);
		if(maxScore>=0.85)
			return 4; //synonyms
		else if(maxScore>=0.65)
			return 3; //somewhat similar
		else if(maxScore>=0.45)
			return 2; //slightly similar
		else if(maxScore>=0.3)
			return 1; //somewhat related but dissimilar
		else return 0;	//unrelated

	}

	private static boolean areAntonyms(String shorter, String longer) {
		if (longer.endsWith(shorter)){
			if(StringUtils.startsWithAny(longer, new String[]{"un", "non", "dis", "mal", "mis", "anti", "de", "il", "im", "in", "ir"}))
				return true;
		}
		if(longer.replace("less", "").equals(shorter.replace("ful", "")))
			return true;
		return false;
	}

	private static ArrayList<String> getDefinitions(String apiResult) throws JSONException {
		if(apiResult==null)
			return null;
		ArrayList<String> definitions = new ArrayList<String>();	

		JSONTokener tokener = new JSONTokener(apiResult);
		JSONObject root = new JSONObject(tokener);
		JSONArray resultsArray= root.getJSONArray("results");

		for(int i=0; i<resultsArray.length(); i++){
			JSONObject result = (JSONObject) resultsArray.get(i);
			try {
				JSONArray sensesArray = result.getJSONArray("senses");
				for (int j = 0; j < sensesArray.length(); j++) {
					JSONObject senses = (JSONObject) sensesArray.get(j);
					try{
						String definition = senses.getString("definition");

						//remove some common stop words from the definitions
						Pattern stopWords = Pattern.compile("\\b(?:with|a|an|in|to|which|that|and|or|but|the|no|of|what|who|which|for)\\b\\s*", Pattern.CASE_INSENSITIVE);
						Matcher matcher1 = stopWords.matcher(definition);
						String def = matcher1.replaceAll("");
						def=def.replaceAll("[\"\\-\\[\\]\\(\\)\\'\\/\\+\\.\\^:,]","");
						//System.out.println("Definition:"+def);
						definitions.add(def);
					} catch(Exception e){

					}
				}
			} catch (Exception e) {
			}
		}
		return definitions;
	}

	private static String getApiResult(String word) throws IOException {
		try{
			String targetURL="http://api.pearson.com/v2/dictionaries/entries?headword="+word;
			URL url = new URL(targetURL);
			InputStreamReader is =  new InputStreamReader(url.openStream());
			BufferedReader bufferedReader = new BufferedReader(is);
			StringBuilder stringBuilder = new StringBuilder();

			String inputLine;
			while ((inputLine = bufferedReader.readLine()) != null){
				stringBuilder.append(inputLine);
				stringBuilder.append(System.lineSeparator());
			}
			bufferedReader.close();
			return stringBuilder.toString().trim();}
		catch(Exception e){
			return null;
		}
	}
}

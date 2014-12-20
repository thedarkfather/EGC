package storing;


import java.sql.ResultSet;
import java.sql.SQLException;

public class Test {

	public static void main(String[]args) throws SQLException{

		StoringInterface.saveVote("voto2", 1);
		ResultSet res = StoringInterface.findAllVotes(1);		
		while(res.next()){
			System.out.println(res.getString("id"));
			System.out.println(res.getString("vote"));
		}
	}
}

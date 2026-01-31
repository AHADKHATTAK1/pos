import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import 'package:logger/logger.dart';
import '../models/user_model.dart';

class AuthService {
  final String baseUrl = "http://localhost:8000/api/v1/auth";
  final logger = Logger();

  Future<Map<String, dynamic>> login(String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse("$baseUrl/login"),
        body: {
          'username': email,
          'password': password,
        },
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        final prefs = await SharedPreferences.getInstance();
        await prefs.setString('access_token', data['access_token']);
        return {'success': true, 'token': data['access_token']};
      } else {
        return {'success': false, 'message': 'Invalid credentials'};
      }
    } catch (e) {
      logger.e("Login error: $e");
      return {'success': false, 'message': 'Server error'};
    }
  }

  Future<Map<String, dynamic>> signup(String name, String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse("$baseUrl/signup"),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'name': name,
          'email': email,
          'password': password,
        }),
      );

      if (response.statusCode == 200) {
        return {'success': true};
      } else {
        final error = json.decode(response.body);
        return {'success': false, 'message': error['detail']};
      }
    } catch (e) {
      logger.e("Signup error: $e");
      return {'success': false, 'message': 'Server error'};
    }
  }

  Future<void> logout() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('access_token');
  }
}

class User {
  final String id;
  final String name;
  final String email;
  final String role;
  final String? businessId;
  final String? storeId;

  User({
    required this.id,
    required this.name,
    required this.email,
    required this.role,
    this.businessId,
    this.storeId,
  });

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      id: json['id'],
      name: json['name'],
      email: json['email'],
      role: json['role'],
      businessId: json['business_id'],
      storeId: json['store_id'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'email': email,
      'role': role,
      'business_id': businessId,
      'store_id': storeId,
    };
  }
}

def validate_data(data):
    """
    Perform data validation steps.
    """
    print("Data Validation:")
    print("Number of Rows:", len(data))
    print("Missing Values:")
    print(data.isnull().sum())

    # Validate data types of columns
    print("\nData Types:")
    print(data.dtypes)

    # Check for outliers
    print("\nOutliers:")
    # Perform outlier detection and print the results

    # Add additional data validation steps here

    # Example: Check for unusual values in a specific column
    print("\nUnusual Values in 'Username' Column:")
    unusual_usernames = data.loc[data['Username'].isin(['admin', 'root', '123456'])]
    print(unusual_usernames)

    # Example: Check for common passwords
    common_passwords = ['password', '123456', 'qwerty']
    common_password_counts = data['Password'].isin(common_passwords).sum()
    print("\nNumber of Common Passwords:", common_password_counts)

    # Example: Check for weak passwords
    weak_password_counts = data['Password'].str.len() < 8
    print("\nNumber of Weak Passwords:", weak_password_counts.sum())

    # Example: Check for commonly used IP addresses
    common_ip_addresses = ['192.168.0.1', '10.0.0.1', '172.16.0.1']
    common_ip_counts = data['IP Address'].isin(common_ip_addresses).sum()
    print("\nNumber of Common IP Addresses:", common_ip_counts)
